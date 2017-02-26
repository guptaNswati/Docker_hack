#!/usr/bin/env bash
for i in /ubuntu_dock/*; do
    ./go/src/github.com/docker/docker/builder/dockerfile/parser/dumper/dumper $i >> /converted/converter_$i
done
