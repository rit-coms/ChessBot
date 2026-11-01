#pragma once

struct Vect2d{
    float x;
    float y;

    Vect2d(float x, float y){
        this->x = x;
        this->y = y;
    }

    Vect2d operator+(const Vect2d &n)
    {
        return Vect2d(x + n.x, y + n.y);
    }

    Vect2d operator-(const Vect2d &n)
    {
        return Vect2d(x - n.x, y - n.y);
    }
};