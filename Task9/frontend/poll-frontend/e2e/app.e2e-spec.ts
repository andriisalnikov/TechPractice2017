import { PollFrontendPage } from './app.po';

describe('poll-frontend App', () => {
  let page: PollFrontendPage;

  beforeEach(() => {
    page = new PollFrontendPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
