namespace mcpserver.Storage
{
    /// <summary>
    /// Provides retrieval-augmented generation (RAG) context lookups for tools executed by the MCP server.
    /// </summary>
    public interface IRagStorage
    {
        /// <summary>
        /// Performs a semantic lookup for the supplied query and returns serialized context.
        /// </summary>
        /// <param name="query">Free-form query text.</param>
        /// <param name="limit">Maximum number of context items to include in the response.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>Serialized context string used to seed downstream LLM prompts.</returns>
        Task<string> SearchAsync(string query, int limit, CancellationToken cancellationToken = default);
    }
}