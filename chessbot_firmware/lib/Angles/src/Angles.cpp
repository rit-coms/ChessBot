#include <math.h>
#include "angles.h"
#include "vector.h"

namespace Angles{
    /** a = forearm length
        b = upper arm length
        c = shortest distance **/
    float inner_angle(float a, float b, float c){
        c = (a+b >= c) ? c : a+b;
        return acos((b*b + c*c - a*a)/(2*b*c));
    }

    Armangles calculate(Vect2d vect){
        float theta = atan2(vect.y, vect.x);
        float c = sqrt(vect.x*vect.x + vect.y*vect.y);
        float alpha = inner_angle(FOREARM, UPPER_ARM, c);

        float beta = inner_angle(UPPER_ARM, c, FOREARM);

        return Armangles{alpha+theta, beta};
    }


}

