#include "Piesa.h"

int Piesa::getId() {
	return this->id;
}

void Piesa::setColor(int color) {
	this->color = color;
}

int Piesa::getColor() {
	return this->color;
}

void Piesa::setAbsolutePin(bool b)
{
	this->absolutePin = b;
}

bool Piesa::getAbsolutePin()
{
	return this->absolutePin;
}

void Piesa::setX(int x) {
	this->x = x;
}

int Piesa::getX() {
	return this->x;
}

void Piesa::setY(int y) {
	this->y = y;
}

int Piesa::getY() {
	return this->y;
}


std::string Piesa::getType()
{
	return this->type;
}

void Piesa::setType(std::string type)
{
	this->type = type;
}

void Piesa::clearIfMovedPieceSeenLst()
{
	ifMovedPieceSeen.clear();
}

void Piesa::addIfMovedPieceSeenLst(Piesa p)
{
	ifMovedPieceSeen.push_back(p);
}

void Piesa::removeIfMovedPieceSeenLst(Piesa p)
{
	for (int i = 0;i < ifMovedPieceSeen.size(); i++)
	{
		if (p == ifMovedPieceSeen[i])
			ifMovedPieceSeen.erase(ifMovedPieceSeen.begin() + i);
	}
}

std::vector<Piesa> Piesa::getIfMovedPieceSeenLst()
{
	return ifMovedPieceSeen;
}

std::vector<std::pair<int, int>> Piesa::getLstMoves()
{
	return this->lstMoves;
}

std::map<std::pair<int, int>, int> Piesa::getWhereToLookIfPathBlocked()
{
	return this->dicWhereToMoveIfPathBlocked;
}

void Piesa::setWhereToLookIfPathBlocked(std::map<std::pair<int, int>, int> dic)
{
	this->dicWhereToMoveIfPathBlocked = dic;
}

void Piesa::setLstMoves(std::vector<std::pair<int, int>> lst)
{
	this->lstMoves = lst;
}

void Piesa::setValue(float value) {
	this->value = value;
}

float Piesa::getValue() {
	return this->value;
}