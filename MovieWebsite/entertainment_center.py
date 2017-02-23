import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar= media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

life_is_beautiful = media.Movie("Life is Beautiful",
                               "When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor and imagination to protect his son from the dangers around their camp.",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
                                "https://www.youtube.com/watch?v=3Y_p7KmAiLM")
                                

#print(avatar.storyline)
#life_is_beautiful.show_trailer()

ratatouille = media.Movie("Ratatouille", "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=md_eEM9BWd8")
midnight_in_paris = media.Movie("Midnight in Paris","While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

nightcrawler = media.Movie("Nightcrawler",
                           "When Louis Bloom, a driven man desperate for work, muscles into the world of L.A. crime journalism, he blurs the line between observer and participant to become the star of his own story. Aiding him in his effort is Nina, a TV-news veteran. ",
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/Nightcrawlerfilm.jpg",
                           "https://www.youtube.com/watch?v=X8kYDQan8bw")

movies = [toy_story, avatar, life_is_beautiful, ratatouille, midnight_in_paris, nightcrawler]

fresh_tomatoes.open_movies_page(movies)
