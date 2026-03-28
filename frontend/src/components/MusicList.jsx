import React from "react";

const MusicList = ({ songs = [], spotify = [] }) => {
  return (
    <div className="container mt-4">

      <h2 className="mb-3">🎵 Recommended for You (YouTube)</h2>

      <div className="row">
        {songs.length > 0 ? (
          songs.map((song, i) => (
            <div className="col-md-4 mb-4" key={i}>
              <div
                className="card h-100 shadow-sm music-card"
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
          ))
        ) : (
          <p>No YouTube songs found</p>
        )}
      </div>

      {/* ================= SPOTIFY SECTION ================= */}
      <h2 className="mt-5 mb-3">🎧 Recommended for You (Spotify)</h2>

      <div className="row">
        {spotify.length > 0 ? (
          spotify.map((song, i) => (
            <div className="col-md-4 mb-4" key={i}>
              <div
                className="card h-100 shadow-sm music-card"
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
                    {song.artist}
                  </p>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No Spotify songs found (Premium Subscription Required)</p>
        )}
      </div>

    </div>
  );
};

export default MusicList;