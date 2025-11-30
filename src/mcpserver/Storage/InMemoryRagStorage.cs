using System.Collections.Concurrent;

namespace mcpserver.Storage
{
    /// <summary>
    /// Minimal in-memory implementation that can satisfy PersonaTool dependencies until a real vector store is wired up.
    /// </summary>
    public sealed class InMemoryRagStorage : IRagStorage
    {
        private readonly ConcurrentDictionary<string, string> _entries = new();

        public Task<string> SearchAsync(string query, int limit, CancellationToken cancellationToken = default)
        {
            if (_entries.IsEmpty)
            {
                return Task.FromResult("No context available yet.");
            }

            var matches = _entries
                .OrderByDescending(entry => GetOverlapScore(entry.Key, query))
                .Take(limit)
                .Select(entry => $"- {entry.Value}")
                .ToArray();

            return Task.FromResult(matches.Length > 0
                ? string.Join("\n", matches)
                : "No relevant context found.");
        }

        /// <summary>
        /// Allows callers or tests to seed context entries.
        /// </summary>
        public void Upsert(string key, string context) => _entries[key] = context;

        private static int GetOverlapScore(string source, string target)
        {
            if (string.IsNullOrWhiteSpace(source) || string.IsNullOrWhiteSpace(target))
            {
                return 0;
            }

            var normalizedSource = source.ToLowerInvariant();
            var normalizedTarget = target.ToLowerInvariant();

            return normalizedTarget.Split(' ').Count(token => normalizedSource.Contains(token));
        }
    }
}