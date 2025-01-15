Results for the Software Interview Problems
===

# Problem - 1

- C++ Docker Image

```
[+] Building 1.3s (10/10) FINISHED                                                                                                                                                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 422B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/gcc:latest                                                                                                                                                                                                                         0.3s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [1/5] FROM docker.io/library/gcc:latest@sha256:d2ae7d55e007c1b50b72d39b6b9e0438c9b50404d77743156cf7498369329b1e                                                                                                                                                                   0.0s
 => => resolve docker.io/library/gcc:latest@sha256:d2ae7d55e007c1b50b72d39b6b9e0438c9b50404d77743156cf7498369329b1e                                                                                                                                                                   0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 278B                                                                                                                                                                                                                                                     0.0s
 => CACHED [2/5] COPY src /usr/src/                                                                                                                                                                                                                                                   0.0s
 => [3/5] COPY Makefile /usr/src/                                                                                                                                                                                                                                                     0.0s
 => [4/5] WORKDIR /usr/src/                                                                                                                                                                                                                                                           0.0s
 => [5/5] RUN make                                                                                                                                                                                                                                                                    0.6s
 => exporting to image                                                                                                                                                                                                                                                                0.2s
 => => exporting layers                                                                                                                                                                                                                                                               0.1s
 => => exporting manifest sha256:0df67e9e7f32f775c2f319d86dd4f9d78465dfb1924469148114b2cbf2153c6b                                                                                                                                                                                     0.0s
 => => exporting config sha256:d9a912f550595e90db53d834e0ddaadd5eeaa95462daafeb15b5e8bd69bf09ad                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:21a6176d751ca8a8c1c685298c1d57d11a7a700d8f7816054d92f4d62a50a5fb                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:f4771aa5dbcb599b5131c12c423019083de3aa49c7083814aeb66ae51a5365e2                                                                                                                                                                                0.0s
 => => naming to docker.io/library/cpp:latest                                                                                                                                                                                                                                         0.0s
 => => unpacking to docker.io/library/cpp:latest
```

-  Python Docker Image

```
[+] Building 0.7s (8/8) FINISHED                                                                                                                                                                                                                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 308B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3                                                                                                                                                                                                                           0.4s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 880B                                                                                                                                                                                                                                                     0.0s
 => CACHED [1/3] FROM docker.io/library/python:3@sha256:a8aab6d8cce4d31c10dda046d6d940fc30b64de3438f7969f0db0ab19f3469f9                                                                                                                                                              0.0s
 => => resolve docker.io/library/python:3@sha256:a8aab6d8cce4d31c10dda046d6d940fc30b64de3438f7969f0db0ab19f3469f9                                                                                                                                                                     0.0s
 => [2/3] COPY src /usr/src/                                                                                                                                                                                                                                                          0.0s
 => [3/3] WORKDIR /usr/src/                                                                                                                                                                                                                                                           0.0s
 => exporting to image                                                                                                                                                                                                                                                                0.1s
 => => exporting layers                                                                                                                                                                                                                                                               0.1s
 => => exporting manifest sha256:c17cbc9e06a74179368291c8aa2af9110be53158efbfea2c670cb8422f90fe06                                                                                                                                                                                     0.0s
 => => exporting config sha256:dabe37f6facede8441ae334cb87da795f3fdcf5a35a120e6bbd14d3dde5a8a19                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:32af49e437d3205727b4c53874d54ae08ab92f32a9be664ad9a421dc6e80ec80                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:5a9ca3e41c3b070054ac47dc472ea84ecee9f7f389638bb6aee369fd731ddf81                                                                                                                                                                                0.0s
 => => naming to docker.io/library/python:latest                                                                                                                                                                                                                                      0.0s
 => => unpacking to docker.io/library/python:latest
```

- Java Docker Image

```
[+] Building 1.1s (10/10) FINISHED                                                                                                                                                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 535B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/maven:latest                                                                                                                                                                                                                       0.3s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [1/5] FROM docker.io/library/maven:latest@sha256:b89ede2635fb8ebd9ba7a3f7d56140f2bd31337b8b0e9fa586b657ee003307a7                                                                                                                                                                 0.0s
 => => resolve docker.io/library/maven:latest@sha256:b89ede2635fb8ebd9ba7a3f7d56140f2bd31337b8b0e9fa586b657ee003307a7                                                                                                                                                                 0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 272B                                                                                                                                                                                                                                                     0.0s
 => CACHED [2/5] COPY src /usr/src/src                                                                                                                                                                                                                                                0.0s
 => CACHED [3/5] COPY pom.xml /usr/src                                                                                                                                                                                                                                                0.0s
 => CACHED [4/5] WORKDIR /usr/src/                                                                                                                                                                                                                                                    0.0s
 => CACHED [5/5] RUN mvn package                                                                                                                                                                                                                                                      0.0s
 => exporting to image                                                                                                                                                                                                                                                                0.7s
 => => exporting layers                                                                                                                                                                                                                                                               0.4s
 => => exporting manifest sha256:438f8268d49220102b5bdc6e7d61feff870d406f11a46711958a8761d4c40d66                                                                                                                                                                                     0.0s
 => => exporting config sha256:54f9a3ffb4837dcd098974ba9c3cd6b5da018bbb2cca2c93d8987d9aa3187805                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:eb460860fe5cdab81549a307803d93db8122ddc1a302a08cc182715c230a7b80                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:4643f105d408deb7f1e69fec6591a7ec938b483a0521377d2bfd82422177342c                                                                                                                                                                                0.0s
 => => naming to docker.io/library/java:latest                                                                                                                                                                                                                                        0.0s
 => => unpacking to docker.io/library/java:latest
```

# Problem - 2

- C++ Build

```
[+] Building 1.3s (10/10) FINISHED                                                                                                                                                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 422B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/gcc:latest                                                                                                                                                                                                                         0.3s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [1/5] FROM docker.io/library/gcc:latest@sha256:d2ae7d55e007c1b50b72d39b6b9e0438c9b50404d77743156cf7498369329b1e                                                                                                                                                                   0.0s
 => => resolve docker.io/library/gcc:latest@sha256:d2ae7d55e007c1b50b72d39b6b9e0438c9b50404d77743156cf7498369329b1e                                                                                                                                                                   0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 278B                                                                                                                                                                                                                                                     0.0s
 => CACHED [2/5] COPY src /usr/src/                                                                                                                                                                                                                                                   0.0s
 => [3/5] COPY Makefile /usr/src/                                                                                                                                                                                                                                                     0.0s
 => [4/5] WORKDIR /usr/src/                                                                                                                                                                                                                                                           0.0s
 => [5/5] RUN make                                                                                                                                                                                                                                                                    0.6s
 => exporting to image                                                                                                                                                                                                                                                                0.2s
 => => exporting layers                                                                                                                                                                                                                                                               0.1s
 => => exporting manifest sha256:0df67e9e7f32f775c2f319d86dd4f9d78465dfb1924469148114b2cbf2153c6b                                                                                                                                                                                     0.0s
 => => exporting config sha256:d9a912f550595e90db53d834e0ddaadd5eeaa95462daafeb15b5e8bd69bf09ad                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:21a6176d751ca8a8c1c685298c1d57d11a7a700d8f7816054d92f4d62a50a5fb                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:f4771aa5dbcb599b5131c12c423019083de3aa49c7083814aeb66ae51a5365e2                                                                                                                                                                                0.0s
 => => naming to docker.io/library/cpp:latest                                                                                                                                                                                                                                         0.0s
 => => unpacking to docker.io/library/cpp:latest
```

- Java Build

```
[+] Building 1.1s (10/10) FINISHED                                                                                                                                                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 535B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/maven:latest                                                                                                                                                                                                                       0.3s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [1/5] FROM docker.io/library/maven:latest@sha256:b89ede2635fb8ebd9ba7a3f7d56140f2bd31337b8b0e9fa586b657ee003307a7                                                                                                                                                                 0.0s
 => => resolve docker.io/library/maven:latest@sha256:b89ede2635fb8ebd9ba7a3f7d56140f2bd31337b8b0e9fa586b657ee003307a7                                                                                                                                                                 0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 272B                                                                                                                                                                                                                                                     0.0s
 => CACHED [2/5] COPY src /usr/src/src                                                                                                                                                                                                                                                0.0s
 => CACHED [3/5] COPY pom.xml /usr/src                                                                                                                                                                                                                                                0.0s
 => CACHED [4/5] WORKDIR /usr/src/                                                                                                                                                                                                                                                    0.0s
 => CACHED [5/5] RUN mvn package                                                                                                                                                                                                                                                      0.0s
 => exporting to image                                                                                                                                                                                                                                                                0.7s
 => => exporting layers                                                                                                                                                                                                                                                               0.4s
 => => exporting manifest sha256:438f8268d49220102b5bdc6e7d61feff870d406f11a46711958a8761d4c40d66                                                                                                                                                                                     0.0s
 => => exporting config sha256:54f9a3ffb4837dcd098974ba9c3cd6b5da018bbb2cca2c93d8987d9aa3187805                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:eb460860fe5cdab81549a307803d93db8122ddc1a302a08cc182715c230a7b80                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:4643f105d408deb7f1e69fec6591a7ec938b483a0521377d2bfd82422177342c                                                                                                                                                                                0.0s
 => => naming to docker.io/library/java:latest                                                                                                                                                                                                                                        0.0s
 => => unpacking to docker.io/library/java:latest
```

- Python Run

```
[+] Building 0.7s (8/8) FINISHED                                                                                                                                                                                                                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                  0.0s
 => => transferring dockerfile: 308B                                                                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3                                                                                                                                                                                                                           0.4s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                       0.0s
 => [internal] load build context                                                                                                                                                                                                                                                     0.0s
 => => transferring context: 880B                                                                                                                                                                                                                                                     0.0s
 => CACHED [1/3] FROM docker.io/library/python:3@sha256:a8aab6d8cce4d31c10dda046d6d940fc30b64de3438f7969f0db0ab19f3469f9                                                                                                                                                              0.0s
 => => resolve docker.io/library/python:3@sha256:a8aab6d8cce4d31c10dda046d6d940fc30b64de3438f7969f0db0ab19f3469f9                                                                                                                                                                     0.0s
 => [2/3] COPY src /usr/src/                                                                                                                                                                                                                                                          0.0s
 => [3/3] WORKDIR /usr/src/                                                                                                                                                                                                                                                           0.0s
 => exporting to image                                                                                                                                                                                                                                                                0.1s
 => => exporting layers                                                                                                                                                                                                                                                               0.1s
 => => exporting manifest sha256:c17cbc9e06a74179368291c8aa2af9110be53158efbfea2c670cb8422f90fe06                                                                                                                                                                                     0.0s
 => => exporting config sha256:dabe37f6facede8441ae334cb87da795f3fdcf5a35a120e6bbd14d3dde5a8a19                                                                                                                                                                                       0.0s
 => => exporting attestation manifest sha256:32af49e437d3205727b4c53874d54ae08ab92f32a9be664ad9a421dc6e80ec80                                                                                                                                                                         0.0s
 => => exporting manifest list sha256:5a9ca3e41c3b070054ac47dc472ea84ecee9f7f389638bb6aee369fd731ddf81                                                                                                                                                                                0.0s
 => => naming to docker.io/library/python:latest                                                                                                                                                                                                                                      0.0s
 => => unpacking to docker.io/library/python:latest
```

# Problem - 3

- C++ Docker Run Output

```
5 4 1 3
```

- Java Docker Run Output

```
5 4 1 3
```

- Python Docker Run Output

```
5 4 1 3
```
