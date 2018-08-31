# econ-sim readme

----

## Project org

### 0.0.1 Goals

1. world is generated from a worldfile

----

## Current docs

### design

A high level description of what the project is / will be.  

#### world

A collection of cells in a sphere-like shape.

#### cell

A cell contains agents, and actions those agents can take.

#### agent

An agent has id, utility, and energy.

#### action

An action costs something and has a result.


### worldfile format

basically json

    {
        "name": "somestring",
        "cells":
            {
                "x_ang, y_ang":
                {
                    "agents":
                    [
                        {
                            "agent_id": 1234567890,
                            "utility": 0,
                            "energy": 0
                        }
                    ],
                    "actions":
                    [
                        {
                            "action_type": "get_mats",
                            "required_mats":
                            [
                                {
                                    "name": "wood",
                                    "count": 10
                                }
                            ]
                        }
                    ]
                }
            }
    }

