import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hash = new HashMap<String, Integer>();
        for(String p : completion) {
            if(!hash.containsKey(p)) {
                hash.put(p, 0);
            }
            hash.put(p, hash.get(p) + 1);
        }
        for(String p : participant) {
            if(!hash.containsKey(p)) { 
                return p;
            }
            hash.put(p, hash.get(p) - 1);
            if(hash.get(p) < 0) {
                return p;
            }
        }
        return null;
    }
}

class SolutionTwo {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hash = new HashMap<>(); // 다이아몬드 연산자
        String result = null;
        for(String p : completion) {
            hash.put(p, hash.getOrDefault(p, 0) + 1); // hashMap.getOrDefault(key, defaultValue);
        }
        for(String p : participant) {
            if(!hash.containsKey(p)) {
                result = p;
                break;
            }
            hash.put(p, hash.get(p) - 1);
            if(hash.get(p) < 0) {
                result = p;
                break;
            }
        }
        return result;
    }
}

// 중복제거
class SolutionThree {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hash = new HashMap<>();
        String result = null;
        for(String p : completion) {
            hash.put(p, hash.getOrDefault(p, 0) + 1);
        }
        for(String p : participant) {
            hash.put(p, hash.getOrDefault(p, 0) - 1);
            if(!hash.containsKey(p) || hash.get(p) < 0) {
                result = p;
                break;
            }
        }
        return result;
    }
}

// 불필요 메서드 제거
class SolutionFour {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hash = new HashMap<>();
        String result = null;
        for(String p : completion) {
            hash.put(p, hash.getOrDefault(p, 0) + 1);
        }
        for(String p : participant) {
            hash.put(p, hash.getOrDefault(p, 0) - 1);
            if(hash.get(p) < 0) {
                result = p;
                break;
            }
        }
        return result;
    }
}