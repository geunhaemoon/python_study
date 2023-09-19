import wordcloud as wc

text = "python python test data user wordcloud"
wcText = wc.WordCloud(font_path="C:\\Windows\\Fonts\\맑은 고딕\\malgun.ttf",
                      background_color="white",
                      stopwords =["test", "data"],
                      min_font_size=10,
                      max_font_size=40

                      )
wcText.generate_from_text(text)
wcText.to_image().show()
# 매번 다른 형태로 이미지 뜸
wcText.to_file("test.png")
