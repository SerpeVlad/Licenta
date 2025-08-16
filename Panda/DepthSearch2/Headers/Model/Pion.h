#pragma once
#include "Piesa.h"

class Pion : public Piesa {
private:
	bool isEnPassant;
	bool isPromoted = false;
public:
	Pion(int id, int x, int y, float value, int color) {
		setX(x);
		setY(y);
		setColor(color);
		setValue(value);
		setType("pion");
	}
	void setIsEnPassant(bool b);
	bool getIsEnPassant();

	// in case of en passant or posible capture
	void addMove(std::pair<int, int> move) override;



	//to be used one after another
	std::vector<std::pair<int, int>> makeLstMoves() override;
	bool getIsPromoted();
};
