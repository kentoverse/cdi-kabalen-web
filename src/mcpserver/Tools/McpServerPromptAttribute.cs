// Tools/McpServerPromptAttribute.cs
// Define the attribute
[AttributeUsage(AttributeTargets.Class)]
public class McpServerPromptAttribute : Attribute
{
}

// Example class using the attribute
[McpServerPrompt]
public class McpServerPrompt
{
    public static string Echo(string message)
    {
        return $"hello {message}";
    }
}