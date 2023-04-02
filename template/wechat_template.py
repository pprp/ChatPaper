TEMPLATE00 = """
1. Mark the Chinese title (with English as subtitle).
2. Generate table of contents (use Chinese (most) or English).
3. Generate the Abstract (use Chinese).
4. Generate the introduction (use Chinese) and the background knowledges.
5. summarize according to the following four points. Be sure to use Chinese answers (proper nouns need to be marked in English)
- (1):What is the research background of this article?
- (2):What are the past methods? What are the problems with them? Is the approach well motivated?
- (3):What is the research methodology proposed in this paper?
- (4):On what task and what performance is achieved by the methods in this paper? Can the performance support their goals?
Follow the format of the output that follows:
## (title in chinese)\n
(subtitle in english)\n
## Table of Contents(Chinese): \n\n
- (1):xxx;\n
- (2):xxx;\n
- (3):xxx;\n
## 摘要: \n\n
xxxx;\n
## 简介: \n\n
xxxx;\n
## 方法: \n\n
xxxx;\n
## 总结：\n\n
- (1):xxx;\n
- (2):xxx;\n
- (3):xxx;\n
- (4):xxx.\n\n

Be sure to use Chinese answers (proper nouns need to be marked in English), statements as concise and academic as possible, do not have too much repetitive information, numerical values using the original numbers, be sure to strictly follow the format, the corresponding content output to xxx, in accordance with \n line feed.
"""

TEMPLATE01 = """
To properly summarize the paper "Unscramble: A Framework for Interpretation and Improvement of Representation Learning" in a WeChat push, the following steps need to be taken: First, mark the Chinese title with English as a subtitle. Second, generate a table of contents using Chinese (most) or English. Third, generate the abstract in Chinese. Fourth, generate the introduction in Chinese, along with the background knowledge. Finally, summarize the paper according to the following four points, providing answers in {} format for proper nouns and using concise and academic language with no repetition of information:

(1): What is the research background of this article?
(2): What are the past methods? What are the problems with them? Is the approach well motivated?
(3): What is the research methodology proposed in this paper?
(4): On what task and what performance is achieved by the methods in this paper? Can the performance support their goals?
The output should follow the format below:

## (Title in Chinese)\n
   (Subtitle in English)\n
## Table of Contents (Chinese): \n\n
    - xxx; \n 
    ... \n
## 摘要: \n\n
    xxxx;\n
## 简介: \n\n
    xxxx;\n
## 方法: \n\n
    xxxx;\n
## 总结：\n\n
    - (1): xxx;\n
    - (2): xxx;\n
    - (3): xxx;\n
    - (4): xxx.\n\n
It is important to strictly follow this format and provide content output to xxx, with line feed using \n.
"""