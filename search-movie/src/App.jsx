import { useState } from "react";
import "./App.css";

function App() {
    const [title, setTitle] = useState("");
    const [site, setSite] = useState("all");
    const [movies, setMovies] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const searchMovies = async () => {
        // if (!title) {
        //     setError("Please enter a movie title.");
        //     return;
        // }

        setLoading(true);
        setError("");

        try {
            let apiUrl = `${window.location.origin}/api/movies/?title=${title}`;
            if (site !== "all") {
                apiUrl += `&site=${site}`;
            }

            const response = await fetch(apiUrl);
            const data = await response.json();

            setMovies(data);
        } catch (error) {
            console.error(error);
            setError("Failed to fetch movies.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            <h1>Film & TV Extractor</h1>

            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search TV or Film"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />

                <select value={site} onChange={(e) => setSite(e.target.value)}>
                    <option value="all">All Sites</option>
                    <option value="fmovies24.to">fmovies24.to</option>
                    <option value="gogoflix.stream">gogoflix.stream</option>
                </select>

                <button onClick={searchMovies} disabled={loading}>
                    {loading ? "Searching..." : "Search"}
                </button>
            </div>

            {error && <p style={{ color: "red" }}>{error}</p>}

            <p>{movies.length} Result(s)</p>

            <div className="results">
                {movies.map((movie, index) => (
                    <div key={index} className="movie-card">
                        <div className="movie-image">
                            <img
                                src={movie.poster_url}
                                alt={movie.title}
                                width="100"
                                onError={(e) => {
                                    // if (e.target.src !== "http://localhost:5173/download.webp") {
                                    e.target.onerror = null; // 避免无限触发
                                    e.target.src = "http://localhost:5173/download.webp"; // ✅ 直接使用本地路径
                                    // }
                                }}
                            />
                        </div>

                        <div className="movie-info">
                            <h3>{movie.title}</h3>
                            <a href={movie.url} target="_blank" rel="noopener noreferrer">
                                {movie.url}
                            </a>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
