#pragma once
#include "vector.h"

int distance(int, int);

namespace Angles {
    //Chess board rn is 80x80, [0,0] is bottom left and the bot is in the middle and 40x40 footprint with the leadscrew in the middle
    const int SQUARE_SIZE = 10;
    const int SCREW_OFFSET = 20;
    const int SCREW_LOCATION_X = 40;
    const int SCREW_LOCATION_Y = -20;
    //Total straight arm length (for test case) = sqrt(95^2 + 35^2) = 101.24228365658293466623451144951
    //Half length = 50.621141828291467333117255724753
    const float UPPER_ARM = 5.75;   //5.75
    const float FOREARM = 8.5;    //8.5

    //initial angle is facing right relative to board
    const float START_ANGLE_UPPER_ARM = 0;
    const float START_ANGLE_FOREARM = 0;

    struct Armangles{
        float shoulder; //angle of upperarm from origin to necessary position
        float elbow; //angle of forearm from upperarm to necessary position
    };

    float inner_angle(float, float, float);
    Armangles calculate(Vect2d);

    
}