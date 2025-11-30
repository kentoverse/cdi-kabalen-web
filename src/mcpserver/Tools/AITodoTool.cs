using mcpserver.Models; // Make sure this namespace matches your Todo model
using mcpserver.Storage; // For TodoStore access

// AI tool for suggesting Todo items
public static class AITodoTool
{
    public static object SuggestTodo(string userInput)
    {
        var todoModel = new mcpserver.Models.Todo
        {
            Id = GenerateNextId(),
            Title = ExtractTitle(userInput)
        };

        // Convert to mcpserver.Storage.Todo

        var todo = new mcpserver.Storage.Todo();
        var missingFields = new List<string>();
        // Assign Title if it exists in Storage.Todo
        var todoType = typeof(mcpserver.Storage.Todo);
        var titleProp = todoType.GetProperty("Title");
        if (titleProp != null)
        {
            titleProp.SetValue(todo, todoModel.Title);
            if (string.IsNullOrWhiteSpace(todoModel.Title)) missingFields.Add("Title");
        }

        if (missingFields.Count > 0)
        {
            return new
            {
                Todo = todo,
                MissingFields = missingFields,
                Prompt = $"Please provide the following missing information: {string.Join(", ", missingFields)}"
            };
        }

        // Add to TodoStore
        TodoStore.Todos.Add(todo);

        return new
        {
            Todo = todo,
            MissingFields = Array.Empty<string>(),
            Prompt = "Todo added successfully."
        };
    }

    private static int GenerateNextId()
    {
        // Simple auto-increment based on count only (since Storage.Todo does not have Id)
        return TodoStore.Todos.Count + 1;
    }

    // Placeholder method for AI extraction logic
    private static string ExtractTitle(string input)
    {
        // Simple heuristic; replace with AI/NLP logic if needed
        return !string.IsNullOrWhiteSpace(input) ? input : "";
    }
}