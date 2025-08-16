#include "Pion.h"

void Pion::setIsEnPassant(bool b)
{
	this->isEnPassant = b;
}

bool Pion::getIsEnPassant()
{
	return this->isEnPassant;
}

void Pion::addMove(std::pair<int, int> move)
{
	std::map<std::pair<int, int>, int> dic = getWhereToLookIfPathBlocked();
	std::vector<std::pair<int, int>> lst = getLstMoves();
	dic[move] = lst.size();
	setWhereToLookIfPathBlocked(dic);
	lst.push_back(move);
	setLstMoves(lst);
}

std::vector<std::pair<int, int>> Pion::makeLstMoves()
{
	if (getAbsolutePin() == false) {
		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();

		if (getY() != 6 && getColor() == 1) {
			std::pair<int, int> move = std::pair<int, int>(getX(), getY() + 1);
			lst.push_back(move);
			dic[move] = 1;
			this->isPromoted = true;
		} // not home square
		else if (getY() == 6 && getColor() == 1) {
			std::pair<int, int> move = std::pair<int, int>(getX(), 5);
			lst.push_back(move);
			dic[move] = 2;
			move = std::pair<int, int>(getX(), 4);
			lst.push_back(move);
			dic[move] = 2;
		} //home square
		setWhereToLookIfPathBlocked(dic);
		setLstMoves(lst);
		return lst;
	}
	else {

		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();
		setWhereToLookIfPathBlocked(dic);
		setLstMoves(lst);
		return lst;
	}

}

bool Pion::getIsPromoted()
{
	return isPromoted;
}
