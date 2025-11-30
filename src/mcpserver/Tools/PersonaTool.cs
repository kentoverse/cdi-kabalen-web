using System.Text.Json;
using System.Text.Json.Serialization;
using mcpserver.Storage;

namespace mcpserver.Tools
{

    public class PersonaTool : ITool
    {
        private readonly AzureOpenAIService? _ai;
        private readonly IRagStorage? _rag;

        public PersonaTool(AzureOpenAIService ai, IRagStorage rag)
        {
            _ai = ai;
            _rag = rag;
        }

        public string Name => "personaAnalysis";

        public async Task<object> RunAsync(object input)
        {
            var payload = JsonSerializer.Deserialize<PersonaInput>(input.ToString()!);

            if (payload == null)
                throw new ArgumentException("Invalid input to personaAnalysis tool.");

            // 1. Retrieve RAG context
            var ragContext = await ((mcpserver.Storage.IRagStorage)_rag).SearchAsync(payload.UserQuery, 5, System.Threading.CancellationToken.None);

            // 2. Construct the persona prompt
            var systemPrompt = mcpserver.Tools.PersonaPrompts.GetPrompt(payload.PersonaStyle);

            var finalPrompt = $@"
You are an AI persona.

Persona Style: {payload.PersonaStyle}

RAG Context:
{ragContext}

User Query:
{payload.UserQuery}
";

            // 3. Call Azure OpenAI
            var response = await _ai.GenerateChatAsync(systemPrompt, finalPrompt);

            return new
            {
                persona = payload.PersonaStyle,
                query = payload.UserQuery,
                response = response
            };
        }

        private class PersonaInput
        {
            [JsonPropertyName("query")]
            public string UserQuery { get; set; }

            [JsonPropertyName("persona")]
            public string PersonaStyle { get; set; }
        }

        public class AzureOpenAIService
        {
            public async Task<string> GenerateChatAsync(string systemPrompt, string userPrompt)
            {
                // TODO: Implement actual call to Azure OpenAI service
                await Task.Delay(10); // Simulate async operation
                return $"[Mocked Response] System: {systemPrompt} | User: {userPrompt}";
            }
        }
    }

    public static class PersonaPrompts
    {
        public static string GetPrompt(string persona)
        {
            return persona switch
            {
                "optimistic" => "Respond with positivity, possibility-thinking, and supportive encouragement.",
                "pessimistic" => "Respond with caution, skepticism, and highlight risks or potential downsides.",
                "neutral" => "Respond with balanced, factual, even-toned reasoning with no emotional charge.",
                _ => "Respond neutrally."
            };
        }
    }
}