# Install script for directory: /Users/pradmc/gnuradio/OOT/gr-custom_resampler/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/custom_resampler" TYPE FILE FILES
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/__init__.py"
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/spline_resampler_fff.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/custom_resampler" TYPE FILE FILES
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/python/__init__.pyc"
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/python/spline_resampler_fff.pyc"
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/python/__init__.pyo"
    "/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/python/spline_resampler_fff.pyo"
    )
endif()

