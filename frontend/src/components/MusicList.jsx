const MusicList = ({ songs }) => {
  return (
    <div>
      <h2>🎵 Recommended for You in YouTube</h2>

      <div className="music-container">

  <div className="row">
  {songs.map((song, i) => (
    <div className="col-md-4 mb-4" key={i}>
      <div
        className="card h-100 shadow-sm"
        style={{ cursor: "pointer" }}
        onClick={() => window.open(song.url, "_blank")}
      >
        <img
          src={song.thumbnail}
          className="card-img-top"
          alt={song.title}
        />

        <div className="card-body text-start">
          <h6 className="card-title">{song.title}</h6>
          <p className="card-text text-muted">
            {song.channel}
          </p>
        </div>
      </div>
    </div>
  ))}
</div>
</div>
    </div>
  );
};

export default MusicList;