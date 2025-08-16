#pragma once
#include "Piesa.h"

class Rege : public Piesa {
private:
	bool k;
	bool q;
public:
	Rege(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("rege");
	}
	std::vector<std::pair<int, int>> makeLstMoves() override;

	void setK(bool k) override { this->k = k; }
	void setQ(bool q) override { this->q = q; }
	bool getK() const override { return k; }
	bool getQ() const override { return q; }
};