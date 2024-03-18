https://philstephens.com/blog/install-jekyll-on-macos-sonoma

Install ruby and chruby using brew:
```
brew install chruby ruby-install xz
ruby-install ruby 3.1.3
```

Configure the shell to use `chruby`:
```
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.1.3" >> ~/.zshrc
```

Verify ruby installation:
```
ruby -v
```

Install Jekyll:
```
gem install jekyll
gem install jekyll-paginate jekyll-feed jekyll-sitemap
```

Finally, run `run.sh`:
```
run.sh
```

Verify the website shows up at `http://127.0.0.1:4000`.
