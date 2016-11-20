# ytsnarf
youtube-dl + ssh solution to "The uploader has not made this video available in your country."

## Installing

`$ pip install ytsnarf `

## Using

```
$ ytsnarf -h <my-host> https://www.youtube.com/watch?v=QH2-TGUlwu4
$ ls
Nyan Cat [original].webm

```

Where `<my-host>` is some Linux machine for which you have an ssh config entry and which has [youtube-dl](https://rg3.github.io/youtube-dl/) installed.

## Configuration

`$ ytsnarf -h <my-host> --save-default`

Creates ~/.ytsnarfrc and records your preferred server to use. With this set up you can now run: `ytsnarf https://www.youtube.com/watch?v=QH2-TGUlwu4`.

## Under The Hood

Here's what `ytsnarf` is doing.

```
$ ytsnarf -h server --verbose https://www.youtube.com/watch?v=QH2-TGUlwu4
[server] run: which youtube-dl
[server] out: /usr/local/bin/youtube-dl
[server] out: 

[server] run: mktemp -d /tmp/ytsnarf-tmp-XXXXXXXX
[server] out: /tmp/ytsnarf-tmp-VGiKQw5f
[server] out: 

[server] run: youtube-dl --no-color --output=/tmp/ytsnarf-tmp-VGiKQw5f/%\(title\)s.%\(ext\)s https://www.youtube.com/watch?v=QH2-TGUlwu4
[server] out: [youtube] QH2-TGUlwu4: Downloading webpage
[server] out: [youtube] QH2-TGUlwu4: Downloading video info webpage
[server] out: [youtube] QH2-TGUlwu4: Extracting video information
[server] out: [download] Destination: /tmp/ytsnarf-tmp-VGiKQw5f/Nyan Cat [original].webm
[server] out: 
[server] out: [download]   0.0% of 7.98MiB at 42.82KiB/s ETA 03:11
[server] out: [download]   0.0% of 7.98MiB at 127.37KiB/s ETA 01:04
[server] out: [download]   0.1% of 7.98MiB at 295.83KiB/s ETA 00:27
[server] out: [download]   0.2% of 7.98MiB at 631.07KiB/s ETA 00:12
[server] out: [download]   0.4% of 7.98MiB at 967.72KiB/s ETA 00:08
[server] out: [download]   0.8% of 7.98MiB at  1.06MiB/s ETA 00:07
[server] out: [download]   1.6% of 7.98MiB at  1.51MiB/s ETA 00:05
[server] out: [download]   3.1% of 7.98MiB at  2.27MiB/s ETA 00:03
[server] out: [download]   6.3% of 7.98MiB at  3.55MiB/s ETA 00:02
[server] out: [download]  12.5% of 7.98MiB at  4.98MiB/s ETA 00:01
[server] out: [download]  25.0% of 7.98MiB at  6.53MiB/s ETA 00:00
[server] out: [download]  50.1% of 7.98MiB at  7.72MiB/s ETA 00:00
[server] out: [download] 100.0% of 7.98MiB at  6.05MiB/s ETA 00:00
[server] out: [download] 100% of 7.98MiB in 00:01
[server] out: 

[server] download: /home/ubuntu/Nyan Cat [original].webm <- /tmp/ytsnarf-tmp-VGiKQw5f/Nyan Cat [original].webm
[server] run: rm -rf /tmp/ytsnarf-tmp-VGiKQw5f
```
