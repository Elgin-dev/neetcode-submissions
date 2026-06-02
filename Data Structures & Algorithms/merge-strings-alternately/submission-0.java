class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();
        int left = 0, right = 0;

        while (left < word1.length() || right < word2.length()) {
            if (left < word1.length()) {
                res.append(word1.charAt(left));
                left++;
            }
            if (right < word2.length()) {
                res.append(word2.charAt(right));
                right++;
            }
        }
        return res.toString();
    }
}
