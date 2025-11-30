// Models/Todo.cs
using System.Xml;

namespace mcpserver.Models
{
    public class Todo
    {
        public int Id { get; set; } = 0;
        public string Title { get; set; } = string.Empty;
        public string? Cause { get; set; } = string.Empty;
        public string? Execute { get; set; } = string.Empty;
        public string? Effect { get; set; } = string.Empty;
        public bool IsCompleted { get; set; } = false;
    }
}