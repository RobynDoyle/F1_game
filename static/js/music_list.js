const audio = document.getElementById('myAudio');
        const musicIcon = document.getElementById('musicIcon');

        // Toggle audio playback
        musicIcon.addEventListener('click', function () {
            if (audio.paused) {
                audio.play();
                musicIcon.classList.remove('fa-play');
                musicIcon.classList.add('fa-pause');
            } else {
                audio.pause();
                musicIcon.classList.remove('fa-pause');
                musicIcon.classList.add('fa-play');
            }
        });

        // Set the initial state of the music icon
        musicIcon.classList.add('fa-play');