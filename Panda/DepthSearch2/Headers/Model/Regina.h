#pragma once
#include "Piesa.h"

class Regina : public Piesa {
public:
	Regina(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("regina");
	}

	std::vector<std::pair<int, int>> makeLstMoves() override;

};
