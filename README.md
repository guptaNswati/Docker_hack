# Utilize Docker Caching

When creating a new image, Docker daemon checks if the already existing images share some layers with the new image, it checks in the /var/lib/docker/ if it has the layers already stored, it uses its cache.

Image layers are Read-Only so multiple images can share layers, but when a container is built it gets its own Write/Read layer too, which enables it to have its own layers on top of what it’s sharing with others (Docker calls it Cow ->"Copy-on-write is a similar strategy of sharing and copying. In this strategy, system processes that need the same data share the same instance of that data rather than having their own copy. At some point, if one process needs to modify or write to the data, only then does the operating system make a copy of the data for that process to use. Only the process that needs to write has access to the data copy. All the other processes continue to use the original data.”)

For checking if layers can be shared among images, docker build check their hash-keys. But lets say there are two dockerfiles with same layers but the order in which layers will be created are different, it would create different hash keys, treating them two different images, not being able to share.

###### Example,
```
- dockerfile_1
from ubuntu
     apt-get install a b c

- dockerfile_2
from ubuntu
     apt-get install b a c
```
As can be seen they are similar files, except the order of layers, so the resulting images would have different hashkeys leading to no sharing.

The goal of this hackathon project is to compare two Dockerfiles, (specifically compare ubuntu images, apt-get layers), to check if they are similar, except in the ordering of the layers and suggest an optimized format for creating the dockerfile in a way that can take advantage of docker caching, saving time and space.

Using dumper, dockerfiles are converted in txt, compared with each other and if found similarites, shows the space consumption and time taken in building these images which could be avoided.

##### Useful docker commands:
- images
- ps -a
- history —no-trunc
- ls /var/lib/docker
- diff -v
- inspect

##### Limitations:
Curretly, it compares only ubuntu images, apt-get layers. And can handle only two files at a time. But can be improved for handling others and more files. Also, it might be more useful at an enterprise level where time and space is most crucial and not at individual level.
