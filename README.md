# ytsnarf
youtube-dl + ssh solution to "The uploader has not made this video available in your country."

# Installing

`$ pip install ytsnarf `

# Using

```
$ ytsnarf -h <my-host> https://www.youtube.com/watch?v=QH2-TGUlwu4
$ ls
Nyan Cat [original].webm

```

Where `<my-host>` is some Linux machine for which you have an ssh config entry and which has [youtube-dl](https://rg3.github.io/youtube-dl/) installed.

# Configuration

`$ ytsnarf -h <my-host> --save-default`

Creates ~/.ytsnarfrc and records your preferred server to use. With this set up you can now run: `ytsnarf https://www.youtube.com/watch?v=QH2-TGUlwu4`.
