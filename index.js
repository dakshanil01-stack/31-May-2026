// Movie Card component (Tailwind CSS ke saath)
const MovieCard = ({ movie }) => (
  <div className="bg-gray-900 rounded-lg overflow-hidden shadow-lg border border-gray-700 hover:scale-105 transition-transform">
    <img src={movie.poster} alt={movie.title} className="w-full h-64 object-cover" />
    <div className="p-4">
      <h3 className="text-white font-bold text-lg">{movie.title}</h3>
      <p className="text-gray-400">{movie.year}</p>
      <button className="mt-3 w-full bg-red-600 text-white py-2 rounded hover:bg-red-700">
        Download
      </button>
    </div>
  </div>
);

// Grid Display
const MovieGrid = ({ movies }) => (
  <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6 p-10 bg-black">
    {movies.map(movie => <MovieCard key={movie.id} movie={movie} />)}
  </div>
);
