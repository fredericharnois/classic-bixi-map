# Classic BIXI Map

![Map of Montreal BIXI stations showing classic bike availability with color-coded icons (red, orange, green) and a legend at the top.](https://i.postimg.cc/D7pwxKMZ/classic-bixi-map-onrender-com-lat-45-5273-lon-73-5704.png)

A web application that displays real-time BIXI bike station data with a focus on classic (non-electric) bikes availability in Montreal.

**Live Demo:** https://classic-bixi-map.onrender.com/ 
*(Note: Hosted on free tier, may be slow and require a few refreshes to load)*

## Background

This project was created out of personal frustration when looking for classic (non-electric) BIXI bikes around Montreal. After seeing multiple Reddit posts mentioning that some docking stations seem to have predominantly electric bikes, I decided to build a tool that would make it easier to find classic bikes specifically.

While the official BIXI app does include a filter for bike types, it doesn't save your preference for displaying only classic bikes - you have to re-apply the filter every time you use the app. This project also served as a learning opportunity to explore map generation and to familiarize myself with working with GBFS (General Bikeshare Feed Specification) feeds.

## Features

- **Classic bikes focus**: Shows all BIXI stations with emphasis on classic bike availability, filtering out electric bikes from the display
- **Interactive map**: Click stations for details, zoom and pan around Montreal, mobile-friendly interface
- **Color-coded markers**: Stations are visually distinguished based on the number of classic bikes available
- **Location services**: Centers map on your current location if permission is granted
- **Station details**: Shows station name and number of available classic bikes
- **Current availability**: Data reflects bike availability at page load time

## Technical Implementation

The application fetches data from BIXI's GBFS (General Bikeshare Feed Specification) feed and displays all stations on an interactive map with color-coded markers based on classic bike availability. The map is generated using Folium, a Python library for creating interactive maps.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.
