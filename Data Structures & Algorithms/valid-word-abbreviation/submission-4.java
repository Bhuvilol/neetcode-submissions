class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0;
        int j = 0;
        while(i<word.length() && j<abbr.length()){
            char wc = word.charAt(i);
            char ac = abbr.charAt(j);
            if(Character.isDigit(ac)){
                if(ac == '0'){
                    return false;
                }
                int cur = 0;
                while(j<abbr.length() && Character.isDigit(abbr.charAt(j))){
                    cur = cur*10 + (abbr.charAt(j)-'0');
                    j++;
                }
                i = i+cur;
            } else {
                if(i >= word.length() || wc!=ac){
                    return false;
                }
                i++;
                j++;
            }
        }
        return i == word.length() && j == abbr.length();
    }
}