namespace mcpserver.Tools
{
    /// <summary>
    /// Represents a discrete executable tool that can be exposed through the MCP server.
    /// </summary>
    public interface ITool
    {
        /// <summary>
        /// Gets the unique name used to register the tool with the MCP server.
        /// </summary>
        string Name { get; }

        /// <summary>
        /// Executes the tool for the supplied payload.
        /// </summary>
        /// <param name="input">The opaque payload provided by the MCP runtime.</param>
        /// <returns>A task that resolves to the tool response.</returns>
        Task<object> RunAsync(object input);
    }
}