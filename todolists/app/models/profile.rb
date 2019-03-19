class Profile < ActiveRecord::Base
  belongs_to :user


  validate :first_last_name_not_null


  def first_last_name_not_null
    if first_name.nil? and last_name.nil?
      errors.add(:first_name, "and last name cannot both be null")
    end
  end

  validates :gender, inclusion: { in: ["male", "female"]}

  validate :no_sue_for_male

  def no_sue_for_male
    if gender == "male" and first_name == "Sue"
      errors.add(:gender, "cannot have first name as 'Sue'")
    end
  end

  def self.get_all_profiles(miny, maxy)
    Profile.where("birth_year BETWEEN :mi and :ma", mi: miny, ma: maxy).order(:birth_year)
  end

end
