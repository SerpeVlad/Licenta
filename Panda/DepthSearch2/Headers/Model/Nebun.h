#pragma once
#include "Piesa.h"

class Nebun : public Piesa {
public:
	Nebun(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("nebun");
	}
	std::vector<std::pair<int, int>> makeLstMoves() override;

};
