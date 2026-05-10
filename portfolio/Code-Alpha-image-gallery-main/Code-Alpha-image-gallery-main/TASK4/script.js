const audio = document.getElementById("audio");
const progress = document.getElementById("progress");
const current = document.getElementById("current");
const duration = document.getElementById("duration");

const title = document.getElementById("title");
const artist = document.getElementById("artist");

let songs = [
  {
    name: "song1.mp3",
    title: "Dreaming",
    artist: "Jay"
  },
  {
    name: "song2.mp3",
    title: "Waves",
    artist: "Nina"
  }
];

let songIndex = 0;

function loadSong(song) {
  title.innerText = song.title;
  artist.innerText = song.artist;
  audio.src = song.name;
}

function togglePlay() {
  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
}

function prevSong() {
  songIndex = (songIndex - 1 + songs.length) % songs.length;
  loadSong(songs[songIndex]);
  audio.play();
}

function nextSong() {
  songIndex = (songIndex + 1) % songs.length;
  loadSong(songs[songIndex]);
  audio.play();
}

function setVolume() {
  const volume = document.getElementById("volume").value;
  audio.volume = volume;
}

function seekSong() {
  audio.currentTime = (progress.value / 100) * audio.duration;
}

audio.addEventListener("timeupdate", () => {
  progress.value = (audio.currentTime / audio.duration) * 100 || 0;

  let min = Math.floor(audio.currentTime / 60);
  let sec = Math.floor(audio.currentTime % 60);
  current.textContent = ${min}:${sec < 10 ? "0" + sec : sec};

  let dmin = Math.floor(audio.duration / 60);
  let dsec = Math.floor(audio.duration % 60);
  if (!isNaN(dmin)) {
    duration.textContent = ${dmin}:${dsec < 10 ? "0" + dsec : dsec};
  }
});

// Autoplay next
audio.addEventListener("ended", nextSong);

// Load the first song
loadSong(songs[songIndex]);