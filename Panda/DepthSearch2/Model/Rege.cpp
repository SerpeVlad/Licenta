#include "Rege.h"

std::vector<std::pair<int, int>> Rege::makeLstMoves() {
	if (getAbsolutePin() == false) {
		std::vector<std::pair<int, int>> lst = std::vector<std::pair<int, int>>();
		std::map<std::pair<int, int>, int> dic = std::map<std::pair<int, int>, int>();

		std::vector<std::pair<int, int>> l = std::vector<std::pair<int, int>>();
		l.push_back(std::pair<int, int>(0, 1));
		l.push_back(std::pair<int, int>(0, -1));
		l.push_back(std::pair<int, int>(1, 0));
		l.push_back(std::pair<int, int>(1, 1));
		l.push_back(std::pair<int, int>(1, -1));
		l.push_back(std::pair<int, int>(-1, 0));
		l.push_back(std::pair<int, int>(-1, 1));
		l.push_back(std::pair<int, int>(-1, -1));

		for (int i = 0;i < l.size();i++) {
			if (0 <= l[i].first + getX() <= 7 && 0 <= l[i].second + getY() <= 7) {
				lst.push_back(std::pair<int, int>(getX() + l[i].first, getY() + l[i].second));
				dic[std::pair<int, int>(getX() + l[i].first, getY() + l[i].second)] = lst.size();
			}
		}

		if(getK()){		
			lst.push_back(std::pair<int, int>(getX() + 2, getY()));
			dic[std::pair<int, int>(getX() + 2, getY())] = lst.size();
		}
		if(getQ()){
			lst.push_back(std::pair<int, int>(getX() - 2, getY()));
			dic[std::pair<int, int>(getX() - 2, getY())] = lst.size();
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
