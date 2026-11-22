# WATER OS — Webots starter simulation

## What this project demonstrates
An original demonstration concept for climate-resilient water recovery:
- stormwater/runoff intake
- virtual water-quality inputs
- adaptive treatment-route decision
- animated water parcels in a 3D transfer pipe
- pump and diversion-valve state changes
- solar-assisted facility representation
- three timed scenarios: heavy rainfall runoff, saline intrusion, and moderate runoff

## Important scientific limits
This is a visual/control-system simulation, not a computational fluid-dynamics model.
The moving blue spheres represent animated water parcels; they are not a physically
accurate fluid simulation. Sensor values are illustrative software inputs, not real
sensor readings. The biological stage is a visual representation only. The simulation
does not prove contaminant removal, drinking-water safety, or treatment efficiency.
Use calibrated sensors and laboratory testing for any real-world performance claims.

## Run in Webots
1. Install Webots from https://cyberbotics.com/
2. Extract the ZIP folder.
3. In Webots choose File > Open World.
4. Open `worlds/water_os_simulation.wbt`.
5. If Webots asks to select a controller, use `water_os_controller`.
6. Press the green Play button.
7. Open the Console / controller output to see scenario decisions.
8. Record your screen while the simulation is running.

## Project structure
- worlds/water_os_simulation.wbt
- controllers/water_os_controller/water_os_controller.py

## Editing the scenarios
Open the Python controller and edit the `scenarios` list. Keep values within
plausible ranges for your chosen demonstration. State clearly that these are
simulated inputs unless connected to calibrated physical sensors.
