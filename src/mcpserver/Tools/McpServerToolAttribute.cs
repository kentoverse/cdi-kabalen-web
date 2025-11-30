// Define the TodoItem class
public class TodoItem
{
    public string Cause { get; set; }
    public string Execute { get; set; }
    public string Effect { get; set; }
    public DateTime? Due { get; set; }
}

// Placeholder attribute for McpServerToolType
[AttributeUsage(AttributeTargets.Class)]
public class McpServerToolTypeAttribute : Attribute
{
}

// Static tool class
[McpServerToolType]
public static class TodoTool
{
    // Shared list for all TodoItems
    private static readonly List<TodoItem> Items = new();

    public static TodoItem Add(string cause, string execute, string effect, DateTime? due)
    {
        var item = new TodoItem
        {
            Cause = cause,
            Execute = execute,
            Effect = effect,
            Due = due
        };

        Items.Add(item);
        return item;
    }

    public static IEnumerable<TodoItem> List() => Items;
}

// Optional wrapper class if you want McpServerTool access
public static class McpServerTool
{
    // Access TodoTool items
    public static IEnumerable<TodoItem> List() => TodoTool.List();
}