const audio = document.getElementById('myAudio');

        function toggleAudio() {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        }
        
