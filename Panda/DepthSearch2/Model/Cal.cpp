#include "Cal.h"

std::vector<std::pair<int, int>> Cal::makeLstMoves() {
	if (getAbsolutePin() == false) {
		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();

		std::vector<std::pair<int, int>> l = std::vector<std::pair<int, int>>();
		l.push_back(std::pair<int, int>(2, 3));
		l.push_back(std::pair<int, int>(2, -3));
		l.push_back(std::pair<int, int>(-2, 3));
		l.push_back(std::pair<int, int>(-2, -3));
		l.push_back(std::pair<int, int>(3, 2));
		l.push_back(std::pair<int, int>(3, -2));
		l.push_back(std::pair<int, int>(-3, 2));
		l.push_back(std::pair<int, int>(-3, -2));

		for (int i = 0;i < l.size();i++) {
			if (0 <= l[i].first + getX() <= 7 && 0 <= l[i].second + getY() <= 7) {
				lst.push_back(std::pair<int, int>(getX() + l[i].first, getY() + l[i].second));
				dic[std::pair<int, int>(getX() + l[i].first, getY() + l[i].second)] = lst.size();
			}
		}

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
