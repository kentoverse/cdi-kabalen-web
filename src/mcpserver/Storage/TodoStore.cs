// Storage/TodoStore.cs

namespace mcpserver.Storage
{
    public static class TodoStore
    {
        public static List<Todo> Todos { get; } = new List<Todo>();
    }

    public class Todo
    {
    }
}