


using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;




namespace mcpserver.Services
{
    public sealed class AzureOpenAIService(HttpClient httpClient, IConfiguration configuration, ILogger<AzureOpenAIService> logger)
    {
        private readonly HttpClient _httpClient = httpClient ?? throw new ArgumentNullException(nameof(httpClient));
        private readonly ILogger<AzureOpenAIService> _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        private readonly string _endpoint = configuration["AzureOpenAI:Endpoint"]
                ?? throw new InvalidOperationException("AzureOpenAI:Endpoint configuration is required.");
        private readonly string _deployment = configuration["AzureOpenAI:Deployment"]
                ?? throw new InvalidOperationException("AzureOpenAI:Deployment configuration is required.");
        private readonly string _apiKey = configuration["AzureOpenAI:ApiKey"]
                ?? throw new InvalidOperationException("AzureOpenAI:ApiKey configuration is required.");
        private readonly string _apiVersion = configuration["AzureOpenAI:ApiVersion"] ?? "2024-02-15-preview";

        public async Task<string> GenerateChatAsync(string systemPrompt, string userPrompt, CancellationToken cancellationToken = default)
        {
            if (string.IsNullOrWhiteSpace(systemPrompt))
            {
                throw new ArgumentException("System prompt must be provided.", nameof(systemPrompt));
            }

            if (string.IsNullOrWhiteSpace(userPrompt))
            {
                throw new ArgumentException("User prompt must be provided.", nameof(userPrompt));
            }

            var url = new Uri(new Uri(_endpoint), $"/openai/deployments/{_deployment}/chat/completions?api-version={_apiVersion}");

            var payload = new
            {
                messages = new object[]
                {
                    new { role = "system", content = systemPrompt },
                    new { role = "user", content = userPrompt },
                }
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, url)
            {
                Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json")
            };
            request.Headers.Add("api-key", _apiKey);

            using var response = await _httpClient.SendAsync(request, cancellationToken).ConfigureAwait(false);

            if (!response.IsSuccessStatusCode)
            {
                var body = await response.Content.ReadAsStringAsync(cancellationToken).ConfigureAwait(false);
                _logger.LogError("Azure OpenAI request failed with status {StatusCode}: {Body}", (int)response.StatusCode, body);
                response.EnsureSuccessStatusCode();
            }

            await using var contentStream = await response.Content.ReadAsStreamAsync(cancellationToken).ConfigureAwait(false);
            using var document = await JsonDocument.ParseAsync(contentStream, cancellationToken: cancellationToken).ConfigureAwait(false);

            if (document.RootElement.TryGetProperty("choices", out var choices) &&
                choices.GetArrayLength() > 0 &&
                choices[0].TryGetProperty("message", out var message) &&
                message.TryGetProperty("content", out var contentElement))
            {
                return contentElement.GetString() ?? string.Empty;
            }

            _logger.LogWarning("Azure OpenAI response did not contain any choices. Raw payload: {Payload}", document.RootElement.ToString());
            return string.Empty;
        }
    }

    // Removed custom IConfiguration interface to fix accessibility and indexing errors
}