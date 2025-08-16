#pragma once
#include "Piesa.h"

class Tura : public Piesa {
public:
	Tura(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("tura");
	}

	std::vector<std::pair<int, int>> makeLstMoves() override;

};
