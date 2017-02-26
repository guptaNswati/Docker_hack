#!/usr/bin/env bash
for i in "./ubuntu_dock/*"; do
    echo $i
    ./go/src/github.com/docker/docker/builder/dockerfile/parser/dumper/dumper $i >> "./converted/converter_$(echo $i | cut -d'/' -f3)"
done
