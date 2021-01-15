cmake_minimum_required(VERSION 3.17)
project(Ex1 C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_FLAGS "-fno-stack-protector -z execstack")
add_executable(Ex1 main.c)