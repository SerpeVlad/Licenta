#pragma once
#include "Piesa.h"

class Cal : public Piesa {
public:
	Cal(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("cal");
	}
	std::vector<std::pair<int, int>> makeLstMoves() override;
};