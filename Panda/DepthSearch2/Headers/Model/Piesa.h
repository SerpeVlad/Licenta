#pragma once
#include <vector>
#include <utility>
#include <map>
#include <string> 

class Piesa {
private:
	int id;
	int x;
	int y;
	float value;
	int color;
	bool absolutePin;
	std::string type;
	std::vector<Piesa> ifMovedPieceSeen;
	std::vector<std::pair<int, int>> lstMoves;
	std::map<std::pair<int, int>, int> dicWhereToMoveIfPathBlocked;
public:
	Piesa() = default;
	Piesa(int id, int x, int y, float value, int color) {
		this->x = x;
		this->y = y;
		this->color = color;
		this->value = value;
		this->absolutePin = false;
	}

	bool operator==(const Piesa& other) const {
		return (this->id == other.id &&
			this->x == other.x &&
			this->y == other.y &&
			this->color == other.color &&
			this->value == other.value &&
			this->type == other.type);
	}

	int getId();

	std::string getType();
	void setType(std::string type);

	void clearIfMovedPieceSeenLst();
	void addIfMovedPieceSeenLst(Piesa p);
	void removeIfMovedPieceSeenLst(Piesa p);
	std::vector<Piesa> getIfMovedPieceSeenLst();


	//to be used one after another
	virtual std::vector<std::pair<int, int>> makeLstMoves();
	virtual void addMove(std::pair<int, int> move); //for pion
	virtual void setK(bool k); // for rege
	virtual void setQ(bool q); // for rege
	virtual bool getK() const; // for rege
	virtual bool getQ() const; // for rege

	std::map<std::pair<int, int>, int> getWhereToLookIfPathBlocked();


	void setWhereToLookIfPathBlocked(std::map<std::pair<int, int>, int> dic);
	void setLstMoves(std::vector<std::pair<int, int>> lst);
	std::vector<std::pair<int, int>> getLstMoves();

	void setValue(float value);
	float getValue();

	void setX(int x);
	int getX();

	void setY(int x);
	int getY();

	void setColor(int color);
	int getColor();

	void setAbsolutePin(bool b);
	bool getAbsolutePin();

};