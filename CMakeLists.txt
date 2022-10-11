cmake_minimum_required(VERSION 3.14)

project(bookish-eureka LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core)
find_package(spdlog CONFIG REQUIRED)
find_package(OpenCV REQUIRED)
add_library(OpenCV INTERFACE IMPORTED)
set_target_properties(OpenCV PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "${OpenCV_INCLUDE_DIRS}"
  INTERFACE_LINK_LIBRARIES "${OpenCV_LIBS}"
)

add_executable(bookish-eureka
  main.cc
)
target_link_libraries(bookish-eureka PRIVATE
  Qt${QT_VERSION_MAJOR}::Core 
  OpenCV
  fmt::fmt
  spdlog::spdlog
)

target_compile_features(bookish-eureka PRIVATE cxx_std_20)

install(TARGETS bookish-eureka
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
