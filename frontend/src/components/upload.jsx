import React, {useState} from "react";
import axios from "axios";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSearch(e) {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    const form = new FormData();
    form.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:8000/search", form, {
        headers: {"Content-Type": "multipart/form-data"}
      });
      setResults(res.data.results || []);
    } catch (err) {
      alert("Search error: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-6">
      <form onSubmit={handleSearch} className="mb-4">
        <input type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])} className="mb-2"/>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded" disabled={loading}>
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {results.map(r => (
          <div key={r.property_id} className="border rounded p-2 shadow">
            <img src={r.image_url} alt={r.title} className="w-full h-48 object-cover rounded"/>
            <h2 className="font-bold mt-2">{r.title}</h2>
            <p>{r.city}, {r.country}</p>
            <p>Price: {r.price}</p>
            <p className="text-sm text-gray-500">Score: {r.score.toFixed(3)}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
