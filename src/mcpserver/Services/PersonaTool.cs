using mcpserver.Services;
using mcpserver.Tools;


public class PersonalTool(AzureOpenAIService azureOpenAIService) : ITool
{
    private readonly AzureOpenAIService _azureOpenAIService = azureOpenAIService;

    string ITool.Name => throw new NotImplementedException();

    Task<object> ITool.RunAsync(object input)
    {
        throw new NotImplementedException();
    }
    // ...
}