from src.scrapperByRequests import Extractor

if __name__ == "__main__":
    bot = Extractor()
    bot.run(num_pages=1)
    bot.export()
